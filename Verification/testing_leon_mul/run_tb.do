#if [file exists "work"] {vdel -all}
#vlib work
transcript file trans/compileTB.txt
onerror {quit}

#vcom -f ../testing_leon_mul/DUT_LEON.f 
vlog +incdir+../testing_leon_mul+../common+../common/inst_h+../common/Tests+../common/sequences ../testing_leon_mul/target_pkg.sv
vlog ../testing_leon_mul/leon_interface.sv
vlog ../testing_leon_mul/top.sv

#+incdir+leon/DUT

#vsim top

#log /* -r
#run -all

quit
