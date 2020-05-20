import os

while (1):
	s = """
[[[ welcome to GUVM user interface ]]]
please choose which dut to compile:
1- Riscy core (based on RISC-v ISA): enter --> 1 
2- Leon core (based on Sparcv8 ISA): enter --> 2
3- Amber core (based on ARM ISA): enter --> 3
if u want to skip compiling DUT and compile test bench only
please choose which dut to verify :
1- Riscy core (based on RISC-v ISA): enter --> 11 
2- Leon core (based on Sparcv8 ISA): enter --> 22
3- Amber core (based on ARM ISA): enter --> 33
if u want to skip all compiling DUT determine which DUT u want to simulate on
please choose which dut to verify :
1- Riscy core (based on RISC-v ISA): enter --> 111
2- Leon core (based on Sparcv8 ISA): enter --> 222
3- Amber core (based on ARM ISA): enter --> 333
any other input will terminate simulation compilation the simulation
DUT: """;
	g = raw_input(s);
	print g;
	if g == "1":
		os.system("vsim -c -do ../testing_riscy/run_riscy.do")
		x=("vsim -c -do \"vsim -novopt top +UVM_TESTNAME=")
	elif g == "2":
		os.system("vsim -c -do ../testing_leon/run_leon.do")
		x=("vsim -c -do \"vsim top +UVM_TESTNAME=")
	elif g == "3":
		os.system("vsim -c -do ../testing_amber/run_amber.do")
		x=("vsim -c -do \"vsim top +UVM_TESTNAME=")
	elif g == "11":
		os.system("vsim -c -do ../testing_riscy/run_tb.do")
		x=("vsim -c -do \"vsim -novopt top +UVM_TESTNAME=")
	elif g == "22":
		os.system("vsim -c -do ../testing_leon/run_tb.do")
		x=("vsim -c -do \"vsim top +UVM_TESTNAME=")
	elif g == "33":
		os.system("vsim -c -do ../testing_amber/run_tb.do")
		x=("vsim -c -do \"vsim top +UVM_TESTNAME=")
	elif g == "111":
		x=("vsim -c -do \"vsim -novopt top +UVM_TESTNAME=")
	elif g == "222":
		x=("vsim -c -do \"vsim top +UVM_TESTNAME=")
	elif g == "333":
		x=("vsim -c -do \"vsim top +UVM_TESTNAME=")
	elif g == "w1":
		os.system("vsim -view vsim.wlf -do ../testing_riscy/wave.do")
	elif g == "w2":
		os.system("vsim -view vsim.wlf -do ../testing_leon/wave.do")
	elif g == "w3":
		os.system("vsim -view vsim.wlf -do ../testing_amber/wave.do")
	else:
		print("please enter a valid number")
		break

	s="""
please choose which test to simulate:
1- add_test (based on RISC-v ISA, Sparcv8 ISA, ARM ISA): enter --> 1 
2- GUVM_test (based on RISC-v ISA, Sparcv8 ISA, ARM ISA): enter --> 2
3- bie_test (based on sparcv8 ISA): enter --> 3
4- child_test (prototype): enter --> 4
5- python_test (prototype): enter --> 5
6- bief_test (sparc v8): enter --> 6
any other input wil terminate the simulation
DUT: """;
	g = raw_input(s);
	print g;
	if g == "1":
		y=("add_test")
		os.system(x+y+" +ARG_INST=A; log /* -r ; run -all ; quit\"")
	elif g == "2":
		y=("GUVM_test")
		os.system(x+y+"; log /* -r ; run -all ; quit\"")
	elif g == "3":
		y=("bie_test")
		os.system(x+y+"; log /* -r ; run -all ; quit\"")
	elif g == "4":
		y=("child_test")
		os.system(x+y+"; log /* -r ; run -all ; quit\"")
	elif g == "5":
		y=("python_test")
		s="""
please choose which instruction to simulate:
1- add (based on RISC-v ISA, Sparcv8 ISA, ARM ISA): enter --> A
2- branch if equal reg-reg (based on RISC-v ISA): enter --> BIER
3- branch if greater than or equal reg-reg signed (based on RISC-v ISA): enter --> BIGTOER
4- branch if less than or equal reg-reg signed (based on RISC-v ISA): enter --> BILTR
5- branch if greater than or equal reg-reg unsigned (based on RISC-v ISA): enter --> BIGTOERU
6- branch if less than or equal reg-reg unsigned (based on RISC-v ISA): enter --> BILTRU
7- Load signed byte with misalignment feat. reg-imm (based on RISC-v ISA): enter --> LSBMA
8- Load signed half with misalignment feat. word reg-imm (based on RISC-v ISA): enter --> LSHMA
9- Load signed byte with misalignment feat. reg-imm (based on RISC-v ISA): enter --> LUBMA
10- Load signed half with misalignment feat. word reg-imm (based on RISC-v ISA): enter --> LUHMA
11- Load word with misalignment feat. reg-imm (based on RISC-v ISA): enter --> LWMA
12- Load word reg-imm (based on Sparcv8 ISA): enter --> LW
13- Load double word reg-imm (based on Sparcv8 ISA): enter --> LDW
14- Load from alternate space reg-reg (based on Sparcv8 ISA): enter --> LWFAS
any other input will simulate no operation or make an error in the simulation
DUT: """;
		z=raw_input(s)
		if z == "1":
			z=("A")
		elif z == "2":
			z=("BIER")
		elif z == "3":
			z=("BIGTOER")
		elif z == "4":
			z=("BILTR")
		elif z == "5":
			z=("BIGTOERU")
		elif z == "6":
			z=("BILTRU")
		elif z == "7":
			z=("LSB")
		elif z == "8":
			z=("LSH")
		elif z == "9":
			z=("LUB")
		elif z == "10":
			z=("LUH")
		elif z == "11":
			z=("LWMA")
		elif z == "12":
			z=("LW")
		elif z == "13":
			z=("LDW")
		elif z == "14":
			z=("LWFAS")
		os.system(x+y+" +ARG_INST="+z+"; log /* -r ; run -all ; quit\"")
	elif g == "6":
		y=("bief_test")
		s="""
please choose which instruction to simulate:
1- branch if equal flag (based on sparc-v8 ISA): enter --> BIEF
2- branch if Negative flag (based on sparc-v8 ISA): enter --> BNEGF
3- branch if carry flag (based on sparc-v8 ISA): enter --> BCSF
4- branch if overflow flag (based on sparc-v8 ISA): enter --> BVSF
any other input will simulate no operation or make an error in the simulation
DUT: """;
		z=raw_input(s)
		if z == "1":
			z=("BIEF")
		elif z == "2":
			z=("BNEGF")
		elif z == "3":
			z=("BCSF")
		elif z == "4":
			z=("BVSF")
		os.system(x+y+" +ARG_INST="+z+"; log /* -r ; run -all ; quit\"")
	elif g == "6":
		y=("subcc_test")
		os.system(x+y+"; log /* -r ; run -all ; quit\"")
	else:
		print("please enter a valid number")
		break
	raw_input('Press any key to start again')
	os.system("cls")