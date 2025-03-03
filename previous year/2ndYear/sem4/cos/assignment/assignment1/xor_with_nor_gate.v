`include "nor_gate.v"
module xor_with_nor_gate(a,b,c);

input a,b;
output c;

wire w1,w2,w3,w4;

nor_gate f1(a,b,w1);
nor_gate f2(a,a,w2);
nor_gate f3(b,b,w3);
nor_gate f4(w2,w3,w4);
nor_gate f5(w1,w4,c);

endmodule