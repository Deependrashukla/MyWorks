module demultiplexer_1to4(a,s0,s1,y0,y1,y2,y3);
input a,s0,s1;
output y0,y1,y2,y3;

assign y0 = (a & ~s0 & ~s1);
assign y1 = (a & s0 & ~s1);
assign y2 = (a & ~s0 & s1);
assign y3 = (a & s0 & s1);

endmodule