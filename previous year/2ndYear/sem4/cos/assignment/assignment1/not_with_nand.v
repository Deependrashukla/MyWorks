`include "nand_gate.v"

module not_with_nand(b,c);
    input b;
    output c;

    nand_gate f1(b,b,c);

endmodule
