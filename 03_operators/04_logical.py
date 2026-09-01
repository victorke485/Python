#diagnostics_indicator = function(count, level, diagnostics_dict, context)
  local icon = level:match("error") and " " or " "
  return " " .. icon .. count
enddiagnostics_indicator = function(count, level, diagnostics_dict, context)
  local icon = level:match("error") and " " or " "
  return " " .. icon .. count
end and - returns true if both the statements are true
# or - returns true if one of the statements is true
# not - reverses the results

print(2 > 3 and 3 < 90)
print(2 > 3 or 3 < 90)
print(not(2 > 3 or 3 < 90))
