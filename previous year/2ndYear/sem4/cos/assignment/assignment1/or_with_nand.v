`include "nand_gate.v"
module or_with_nand(a,b,c);

input a,b;
output c;

wire w1,w2;

nand_gate f1(a,a,w1);
nand_gate f2(b,b,w2);
nand_gate f3(w1,w2,c);


endmodule