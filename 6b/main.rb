# Prompt https://adventofcode.com/2018/day/4

require "awesome_print"

class Step
    attr_accessor :prereqs, :unlocks, :letter, :health

    def initialize
        letter = ''
        health = 0
        @prereqs = []
        @unlocks = []
    end
end

graph = Hash.new { |h,k| h[k] = Step.new }

# Build my quick shoddy version of a "graph"
File.readlines("input.txt").each do |step|
    parsed_step = /Step (\w) must be finished before step (\w) can begin./.match(step.strip())
    prereq = parsed_step.captures[0]
    target = parsed_step.captures[1]
    graph[prereq].letter = prereq
    graph[target].letter = target
    graph[prereq].health = prereq.ord - 64 + 60
    graph[target].health = target.ord - 64 + 60

    graph[target].prereqs << graph[prereq]
    graph[prereq].unlocks << graph[target]
end

# Select all starting points with no prereqs
starting_point = graph.select {|k,v| v.prereqs == []}.sort.map(&:first)

answer = []

queue = [starting_point].flatten

# Every iteration is a second. Reduce one health for every second until it's empty
# Probably not the most efficient way to do it but... 
seconds = 0
while queue.length > 0
    queue.sort!
    five_workers = queue[0..4]
    five_workers.each do |working_letter|
        graph[working_letter].health -= 1
        if graph[working_letter].health <= 0
            letter = queue.delete(working_letter)
            answer << letter
            graph[letter].unlocks.map(&:letter).each do |unlock|
                queue << unlock if (graph[unlock].prereqs.map(&:letter) - answer).length.zero?
            end
        end
    end
    seconds += 1
end

graph.each do |h,k|
    puts "Letter: #{h} Prereqs: #{k.prereqs.map(&:letter)}"
end

puts seconds