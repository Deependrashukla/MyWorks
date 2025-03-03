`include "nor_gate.v"
module or_with_nor_gate(a,b,c);

input a,b;
output c;

wire w1,w2;

nor_gate f1(a,b,w1);
nor_gate f2(w1,w1,c);

endmodule
