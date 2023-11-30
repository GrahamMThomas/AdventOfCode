# Prompt https://adventofcode.com/2018/day/4

require 'awesome_print'

class Node
  attr_accessor :children, :metadata_entries, :num_of_children, :num_of_metadata

  def initialize()
    @num_of_children = 0
    @num_of_metadata = 0
    @children = []
    @metadata_entries = []
  end

  def get_children(tree)
    total_metadata = 0
    @num_of_children = tree.get_next_input
    @num_of_metadata = tree.get_next_input
    num_of_children.times do |x|
      bob = Node.new
      total_metadata += bob.get_children(tree)
      total_metadata += bob.get_metadata(tree)
      @children << bob
    end
    total_metadata
  end

  def get_metadata(tree)
    @num_of_metadata.times do |x|
      @metadata_entries << tree.get_next_input
    end
    @metadata_entries.sum
  end

  def get_value
    if @num_of_children.zero?
      puts "Returning #{@metadata_entries.sum}"
      return @metadata_entries.sum
    end

    total_value = 0
    ap @children
    @metadata_entries.each do |value|
      unless @children[value - 1].nil?
        puts "Getting value for #{value}"
        total_value += @children[value - 1].get_value
        puts total_value
      end
    end
    total_value
  end
end

class Tree
  attr_accessor :input_pointer, :input, :root

  def initialize(input)
    @input = input.split(' ').map(&:to_i)
    @input_pointer = 0
  end

  def get_next_input
    tmp = @input[@input_pointer]
    @input_pointer += 1
    tmp
  end

  ## Part 1 method
  def get_metadata_sum
    @root = Node.new
    total_metadata = @root.get_children(self)
    total_metadata += @root.get_metadata(self)
    total_metadata
  end
end

# Build my quick shoddy version of a "graph"
input = File.open('input.txt').read

bob = Tree.new(input)
bob.get_metadata_sum
puts "Answer is: #{bob.root.get_value}"
