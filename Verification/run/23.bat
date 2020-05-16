
vsim -c -do "transcript file trans/run.txt;vsim top +UVM_TESTNAME=bie_test ; log /* -r ; run -all ; quit"
