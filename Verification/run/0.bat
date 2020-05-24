
vsim -c -do "transcript file trans/run.txt;vsim top +UVM_TESTNAME=mul_test +ARG_INST=UMULR ; log /* -r ; run -all ; quit"
