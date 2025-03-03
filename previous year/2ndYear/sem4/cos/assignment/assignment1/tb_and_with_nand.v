`include "and_with_nand.v"

module tb_and_with_nand;

reg a,b;
wire c;

and_with_nand t1(a,b,c);

initial begin
    $monitor("input=%b, input=%b, output=%b\n", a, b, c);
    #2 a=1'b0; b=1'b0;
    #2 a=1'b1; b=1'b0;
    #2 a=1'b0; b=1'b1;
    #2 a=1'b1; b=1'b1;
end

initial begin
 $dumpfile("out.vcd");
 $dumpvars;
 #10 $finish;
end

endmodule