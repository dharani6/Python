package main

import (
	"fmt"
	"strings"
	"testing"
	"time"

	"github.com/reiver/go-telnet"
)

type Router struct {
	Host string
	Port string
}

var R1 = Router{
	Host: "localhost",
	Port: "5004",
}

var R2 = Router{
	Host: "localhost",
	Port: "5005",
}

// Connect to router
func connectRouter(r Router) (*telnet.Conn, error) {
	address := r.Host + ":" + r.Port

	conn, err := telnet.DialTo(address)
	if err != nil {
		return nil, err
	}

	time.Sleep(1 * time.Second)

	return conn, nil
}

// Send command to router
func sendCommand(conn *telnet.Conn, command string) (string, error) {

	_, err := conn.Write([]byte(command + "\r\n"))
	if err != nil {
		return "", err
	}

	time.Sleep(1 * time.Second)

	buffer := make([]byte, 8192)

	n, err := conn.Read(buffer)
	if err != nil {
		return "", err
	}

	return string(buffer[:n]), nil
}

// Configure interface shutdown
func shutdownInterface(conn *telnet.Conn, interfaceName string) error {

	commands := []string{
		"enable",
		"configure terminal",
		"interface " + interfaceName,
		"shutdown",
		"end",
	}

	for _, cmd := range commands {
		_, err := sendCommand(conn, cmd)
		if err != nil {
			return err
		}
	}

	return nil
}

// Configure interface no shutdown
func noShutdownInterface(conn *telnet.Conn, interfaceName string) error {

	commands := []string{
		"enable",
		"configure terminal",
		"interface " + interfaceName,
		"no shutdown",
		"end",
	}

	for _, cmd := range commands {
		_, err := sendCommand(conn, cmd)
		if err != nil {
			return err
		}
	}

	return nil
}

func TestLACPMemberFailure(t *testing.T) {

	// Connect to R1
	conn, err := connectRouter(R1)

	if err != nil {
		t.Fatalf("Failed to connect to R1: %v", err)
	}

	defer conn.Close()

	// Shutdown LACP member
	err = shutdownInterface(
		conn,
		"GigabitEthernet1/0",
	)

	if err != nil {
		t.Fatalf("Failed to shutdown interface: %v", err)
	}

	// Always restore interface
	defer func() {

		err := noShutdownInterface(
			conn,
			"GigabitEthernet1/0",
		)

		if err != nil {
			t.Errorf(
				"Failed to restore interface: %v",
				err,
			)
		}

	}()

	// Check LACP member
	output, err := sendCommand(
		conn,
		"show interfaces Port-channel 1 | include Member",
	)

	if err != nil {
		t.Fatalf("Failed to execute show command: %v", err)
	}

	fmt.Println(output)

	// Verify second member exists
	if !strings.Contains(
		output,
		"GigabitEthernet2/0",
	) {
		t.Errorf(
			"Expected GigabitEthernet2/0 to remain in Port-channel. Output:\n%s",
			output,
		)
	}

	// Ping R2
	pingOutput, err := sendCommand(
		conn,
		"ping 10.10.10.2",
	)

	if err != nil {
		t.Fatalf("Ping command failed: %v", err)
	}

	fmt.Println(pingOutput)

	// Verify ping success
	if !strings.Contains(
		pingOutput,
		"Success rate is 100",
	) {
		t.Errorf(
			"Ping failed. Output:\n%s",
			pingOutput,
		)
	}
}
