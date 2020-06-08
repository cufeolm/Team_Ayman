
::vsim -c -do "transcript file trans/run.txt;vsim top +UVM_TESTNAME=arith_flag_test +ARG_INST=ADDX; log /* -r ; run -all ; quit"
::vsim -c -do "transcript file trans/run.txt;vsim top +UVM_TESTNAME=add_test +ARG_INST=A ; log /* -r ; run -all ; quit"

::vsim -c -do "transcript file trans/run.txt;vsim top +UVM_TESTNAME=arith_flag_amber_test +ARG_INST=SUBBCC; log /* -r ; run -all ; quit"
vsim -c -do "transcript file trans/run.txt;vsim top +UVM_TESTNAME=arith_flag_amber_test +ARG_INST=ADDCC; log /* -r ; run -all ; quit"