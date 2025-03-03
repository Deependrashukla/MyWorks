`include "nor_gate.v"
module not_with_nor_gate(a,c);

input a;
output c;

nor_gate f1(a,a,c);


endmodule