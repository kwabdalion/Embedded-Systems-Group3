from trafficlight import StateMachine

def start_transitions(input):
	if input == "100001":
		newState = "goN"
	elif input == "100010":
		newState = "waitN"
	elif input == "001100":
		newState = "goE"
	elif input == "010100":
		newState = "waitE"
	else:
		newState = "error_state"
	return (newState, input)

def goN_state_transitions(input):
	if input == "00" or input == "10":
		newState = "goN"
	elif input == "01" or input == "11":
		newState = "waitN"
	else:
		newState = "error_state"
	return (newState, input)

def waitN_state_transitions(input):
	if input == "00" or input == "01" or input == "10" or input == "11":
		newState = "goE"
	else:
		newState = "error_state"
	return (newState, input)

def goE_state_transitions(input):
	if input == "00" or input == "01":
		newState = "goE"
	elif input == "10" or input == "11":
		newState = "waitE"
	else:
		newState = "error_state"
	return (newState, input)

def waitE_state_transitions(input):
	if input == "00" or input == "01" or input == "10" or input == "11":
		newState = "goN"
	else: 
		newState = "error_state"
	return (newState, input) 

if __name__ == "__main__":
	m = StateMachine()
	m.add_state("Start", start_transitions)
	m.add_state("goN",  goN_state_transitions)
	m.add_state("waitN", waitN_state_transitions)
	m.add_state("goE", goE_state_transitions)
	m.add_state("waitE", waitE_state_transitions)
	m.add_state("waitE", None, end_state = 1)
	m.set_start("Start")
	print(m.handlers)
	m.run("100001")
#	m.run("10")
#	m.run("00")
#	m.run("01")
#	m.run("11")
#	m.run("01")
#	m.run("11")
#	m.run("10")

