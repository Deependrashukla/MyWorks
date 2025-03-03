`include "nor_gate.v"
module and_with_nor_gate(a,b,c);

input a,b;
output c;

wire w1,w2;

nor_gate f1(a,a,w1);
nor_gate f2(b,b,w2);
nor_gate f3(w1,w2,c);

endmodule