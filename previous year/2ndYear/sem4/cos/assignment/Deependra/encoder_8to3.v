module encoder(a7,a6,a5,a4,a3,a2,a1,a0,y2,y1,y0);
input a7,a6,a5,a4,a3,a2,a1,a0;
output y2,y1,y0;

assign y2 = a7 | a6 | a5 | a4;
assign y1 = a7 | a6 | a3 | a2;
assign y0 = a7 | a5 | a3 | a1;

endmodule