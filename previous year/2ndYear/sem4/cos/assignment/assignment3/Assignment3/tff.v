module tff(clk,rst,t,q,b_q);
  input t,clk,rst;
  output wire b_q;
  output reg q;
  
  assign b_q = ~q;
  
  always @(posedge clk)
    begin
      if(rst)
        q<=0;
      else
        begin
          if(t==1)
            q<=(~q);
          else
            q<=q;
        end
    end
endmodule
