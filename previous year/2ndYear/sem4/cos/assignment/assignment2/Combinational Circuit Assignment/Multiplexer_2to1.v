module multiplexer(ab,sel,c);
input [1:0]ab;
input sel;
output c;

assign c = (sel) ? ab[1]:ab[0];

endmodule