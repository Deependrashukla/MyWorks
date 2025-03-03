`include "notgate.v"
module tb_notgate;
reg a;
wire c;
notgate f1(a,c);

initial begin
    $monitor("input=%b, output=%b\n", a, c);
    #2 a=1'b0;
    #2 a=1'b1;
    #2 a=1'b0;
    #2 a=1'b1;
end

initial begin
 $dumpfile("Out.vcd");
 $dumpvars;
 #100 $finish;
end

endmodule
