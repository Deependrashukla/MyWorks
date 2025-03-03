module bit3_comparator(a2,a1,a0,b2,b1,b0,gt,eq,lt);

input a2,a1,a0,b2,b1,b0;
output gt,eq,lt;

assign gt = (a2 > b2) ? 1 :
            (a2 == b2 && a1 > b1) ? 1 :
            (a2 == b2 && a1 == b1 && a0 > b0) ? 1 : 0;
assign eq = (a2 == b2) ? ((a1 == b1) ? ((a0 == b0) ? 1 : 0) : 0) : 0;
assign lt = (a2 < b2) ? 1 :
            (a2 == b2 && a1 < b1) ? 1 :
            (a2 == b2 && a1 == b1 && a0 < b0) ? 1 : 0;
            
endmodule

