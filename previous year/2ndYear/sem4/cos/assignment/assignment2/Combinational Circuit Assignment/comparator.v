
module bit3_comparator(
    input [2:0] a,
    input [2:0] b,
    output gt,
    output eq,
    output lt
);

assign gt = (a > b) ? 1 : 0;

assign eq = (a == b) ? 1 : 0;

assign lt = (a < b) ? 1 : 0;

endmodule

