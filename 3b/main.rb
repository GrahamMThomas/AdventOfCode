require "awesome_print"

class SquareInch
    attr_accessor :claims

    def initialize
        @claims = []
    end
end

fabric = Array.new(1000) { Array.new(1000) {SquareInch.new}}

File.readlines("input.txt").each do |claim|
    # Parsing ===================================================================
    parsed_claim = /#(\d+) @ (\d+),(\d+): (\d+)x(\d+)/.match(claim.strip())
    claim_id = parsed_claim.captures[0].to_i
    from_left_edge = parsed_claim.captures[1].to_i
    from_top_edge = parsed_claim.captures[2].to_i
    width = parsed_claim.captures[3].to_i
    height = parsed_claim.captures[4].to_i

    # Iteration =================================================================
    (0...width).each do |x_coord|
        (0...height).each do |y_coord|
                fabric[x_coord + from_left_edge][y_coord+from_top_edge].claims << claim_id
        end
    end
end

overlapping_inches = (0...1000).map do |x_coord|
    fabric[x_coord].select {|claim| claim.claims.length >= 2}
end

puts "Answer #{overlapping_inches.flatten.count}"