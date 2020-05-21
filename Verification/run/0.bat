
vsim -c -do "transcript file trans/run.txt;vsim top +UVM_TESTNAME=addxcc_test ; log /* -r ; run -all ; quit"
