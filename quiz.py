listeFragen = ['Question No : 1 - Which of the following statements is true when querying the extended attributes of a file that has no extended attributes set?']
listeAntworten = [
  [ "Question No : 1 - Which of the following statements is true when querying the extended attributes of a file that has no extended attributes set?",
  "A. getfattr will print a warning and exit with a value of 0.",
  "B. getfattr will print a warning and exit with a value of 1.",
  "C. No output will be produced and getfattr will exit with a value of 0.",
  "D. No output will be produced and getfattr will exit with a value of 1."],
  ["Question No : 2 - Which directive must be set to 0 in a host or service definition to prevent Nagios from sending more than one alert for a particular event? (Specify only the directive without any options or parameters)."]
]

for len(listeAntworten):
  for item in listeAntworten[0][1:]:
    print (item)
