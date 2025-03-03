`include "orByNand.v"
module tb_orByNand;
reg a,b;
wire c;
orByNand f1(a,b,c);
orByNand f2(a,b,c);
orByNand f3(a,b,c);

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
 #100 $finish;
end

endmodule
