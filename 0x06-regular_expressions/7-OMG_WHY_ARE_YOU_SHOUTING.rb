#!/usr/bin/env ruby
# Script expression that must be only matching capital letters

puts ARGV[0].scan(/[A-Z]/).join
