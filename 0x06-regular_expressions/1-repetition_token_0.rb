#!/usr/bin/env ruby
# Find the regular expression that will match the cases

puts ARGV[0].scan(/hbt{2,5}n/).join
