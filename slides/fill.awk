# Fills the {{name}} marks of the speaker script with the values of the paper's macros.
#   awk -f fill.awk ../paper_A/numbers.tex paper_text.tex talk_notes.src.md > talk_notes.md
# A mark without a macro stops the build.

/^\\newcommand\{\\[A-Za-z]+\}\{.*\}$/ {
  name = $0
  sub(/^\\newcommand\{\\/, "", name)
  sub(/\}.*$/, "", name)
  val = $0
  sub(/^\\newcommand\{\\[A-Za-z]+\}\{/, "", val)
  sub(/\}$/, "", val)
  gsub(/\\%/, "%", val)
  gsub(/\{,\}/, ",", val)
  value[name] = val
  next
}

FILENAME ~ /\.src\.md$/ {
  line = $0
  out = ""
  while (match(line, /\{\{[A-Za-z]+\}\}/)) {
    key = substr(line, RSTART + 2, RLENGTH - 4)
    if (!(key in value)) {
      print "fill.awk: no macro named " key > "/dev/stderr"
      bad = 1
      value[key] = "??"
    }
    out = out substr(line, 1, RSTART - 1) value[key]
    line = substr(line, RSTART + RLENGTH)
  }
  print out line
}

END { exit bad }
