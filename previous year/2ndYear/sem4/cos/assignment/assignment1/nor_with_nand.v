`include "nand_gate.v"

module nor_with_nand(a,b,c);
    input a,b;
    output c;

    wire w1,w2,w3;

    nand_gate f1(a,b,w1);
    nand_gate f2(a,b,w2);
    nand_gate f3(w1,w2,w3);
    nand_gate f4(w3,w3,c);

endmodule
