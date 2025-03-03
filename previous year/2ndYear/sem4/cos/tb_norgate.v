`include "norgate.v"
module tb_nandgate;
reg a,b;
wire c;
norgate f1(a,b,c);

initial begin
    $monitor("input=%b, input=%b, output=%b\n", a, b, c);
    #2 a=1'b0; b=1'b0;
    #2 a=1'b1; b=1'b0;
    #2 a=1'b0; b=1'b1;
    #2 a=1'b1; b=1'b1;
end

initial begin
 $dumpfile("Out.vcd");
 $dumpvars;
 #100 $finish;
end

endmodule
