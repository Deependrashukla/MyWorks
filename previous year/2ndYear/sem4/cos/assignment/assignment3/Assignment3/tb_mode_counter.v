`include "mode_counter.v"

module tb_model_counter();
reg clk, reset,mode;
wire [15:0]counter;

mode_counter #(.size(16)) c1(clk, reset,mode,  counter);

initial begin
clk <= 1;
forever begin
#1 clk <= ~clk;
end
end

initial begin
$monitor("counter=%d", counter);

reset = 1'b1; 
mode=1'd0;
#2 reset = 1'b0;
#29 mode=1'd1;
#29 $finish;

end

initial begin
    $dumpfile("out.vcd");
    $dumpvars;
    #70 $finish;

  end
endmodule