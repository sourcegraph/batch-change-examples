#! /usr/bin/env ruby        

require 'yaml'

content = YAML.load(ARGF.read)
content['services'].each do |name, vals|
  vals["entrypoint"].is_a?(Array) && vals["entrypoint"] << "--debug"
  vals["entrypoint"].is_a?(String) && vals["entrypoint"] += " --debug"
end
puts content.to_yaml