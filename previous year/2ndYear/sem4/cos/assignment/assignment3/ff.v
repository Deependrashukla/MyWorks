module dff (d,clk,q,qb);
    input d,clk;
    output q,qb;
    reg q,qb;
    begin
        q=1'b0;
        qb = 1'b1;

    end

    always @ (posedge clk)
        begin
            q=d;
            qb=~q;
        end

endmodule