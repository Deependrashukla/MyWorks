module ternary (a, b, c, d);

input (a, b, c);
output d;
assign d = c ? b:a
endmodule