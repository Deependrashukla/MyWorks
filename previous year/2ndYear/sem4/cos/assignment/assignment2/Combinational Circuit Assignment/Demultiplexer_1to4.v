module demux1_4(in,sel,out);
input in;
input [1:0] sel;
output [3:0] out;


assign out = (sel == 2'b00) ? {in, 3'b000} :
             (sel == 2'b01) ? {3'b0, in, 2'b00} :
             (sel == 2'b10) ? {3'b00, in, 1'b0} :
             (sel == 2'b11) ? {3'b000, in} :
             4'b0000;
endmodule
