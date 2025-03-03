module multiplexer(a,b,sel,c);
input a,b,sel;
output c;

assign c = (sel) ? b:a;

endmodule