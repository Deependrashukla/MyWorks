`include "comparator.v"

module tb_3bit_comparator;
reg a2,a1,a0,b2,b1,b0;
wire gt,eq,lt;

bit3_comparator f1(a2,a1,a0,b2,b1,b0,gt,eq,lt);
initial begin
    $monitor("a2=%b, a1=%b, a0=%b, b2=%b, b1=%b, b0=%b, output=%b%b%b\n", a2,a1,a0,b2,b1,b0,gt,eq,lt);
    #2 a2=1; a1=1; a0=1; b2=0; b1=0; b0=0;
    #2 a2=0; a1=0; a0=0; b2=1; b1=1; b0=1;
    #2 a2=1; a1=1; a0=1; b2=1; b1=1; b0=1;
    #2 a2=1; a1=0; a0=0; b2=0; b1=0; b0=0;
    #2 a2=1; a1=1; a0=0; b2=1; b1=1; b0=0;
    #2 a2=0; a1=1; a0=1; b2=1; b1=1; b0=1;
    #2 a2=0; a1=0; a0=0; b2=0; b1=0; b0=1;

end

initial begin
 $dumpfile("out.vcd");
 $dumpvars;
 #100 $finish;
end

endmodule