export const templates = [
  {id:"thought_bubble",name:"Human Crisis / Pet Priority",family:"contrast",description:"Human worried. Pet thinking about something trivial.",required:["pet_image","recipient_name"],occasions:[]},
  {id:"pet_standup",name:"Pet Stand-Up",family:"status_inversion",description:"Pet at a microphone roasting the owner.",required:["pet_image","recipient_name"],occasions:[]},
  {id:"breaking_news",name:"Breaking News",family:"documentary",description:"Fake news broadcast about the recipient.",required:["recipient_name"],occasions:[]},
  {id:"performance_review",name:"Pet Performance Review",family:"status_inversion",description:"Pet evaluates owner like an employee.",required:["pet_image","recipient_name"],occasions:[]},
  {id:"pet_therapist",name:"Pet Therapist",family:"status_inversion",description:"Pet diagnoses the owner.",required:["pet_image","recipient_name"],occasions:[]},
  {id:"search_history",name:"Pet Search History",family:"observation",description:"Browser search queries from the pet.",required:["pet_image","recipient_name"],occasions:[]},
  {id:"complaint_dept",name:"Pet Complaint Department",family:"status_inversion",description:"Pet files official complaint.",required:["pet_image","recipient_name"],occasions:[]},
  {id:"split_panel",name:"Human vs Pet Priorities",family:"contrast",description:"Split-screen: human concern vs pet.",required:["pet_image","recipient_name"],occasions:[]},
  {id:"incident_report",name:"Official Incident Report",family:"documentary",description:"Incident report about the recipient.",required:["recipient_name"],occasions:[]},
  {id:"wildcard",name:"Wildcard Roast",family:"mixed",description:"We choose the funniest format.",required:["pet_image","recipient_name","facts"],occasions:[]},
  {id:"xmas_santa_automated",name:"Santa Automated",family:"status_inversion",description:"Santa reads automated notice.",required:["recipient_name"],occasions:["christmas"]},
  {id:"xmas_santa_vs_robots",name:"Santa vs Robots",family:"documentary",description:"Robots disabled in sleigh attack.",required:["recipient_name"],occasions:["christmas"]},
  {id:"xmas_elf_redundancy",name:"Elf Redundancy",family:"corporate",description:"North Pole restructuring.",required:["recipient_name"],occasions:["christmas"]},
  {id:"xmas_pet_security",name:"Pet Security Failure",family:"observation",description:"Dog accepted biscuit. Investigation closed.",required:["recipient_name"],occasions:["christmas"]},
  {id:"xmas_performance_review",name:"Christmas Review",family:"corporate",description:"Pet reviews Christmas performance.",required:["recipient_name"],occasions:["christmas"]},
  {id:"xmas_human_vs_pet",name:"Human vs Pet Xmas",family:"contrast",description:"AGI worry vs turkey focus.",required:["recipient_name"],occasions:["christmas"]},
  {id:"xmas_cat_vs_tree",name:"Cat vs Tree",family:"documentary",description:"Tree destroyed 14 min after deployment.",required:["recipient_name"],occasions:["christmas"]},
  {id:"xmas_santa_search_history",name:"Santa Reads History",family:"observation",description:"Santa horrified, pet smug.",required:["recipient_name"],occasions:["christmas"]},
  {id:"xmas_ai_card",name:"AI Christmas Card",family:"meta",description:"Card is from an AI.",required:["recipient_name"],occasions:["christmas"]},
  {id:"xmas_pet_complaint",name:"Pet Complaint to Santa",family:"status_inversion",description:"Requesting replacement owner.",required:["recipient_name"],occasions:["christmas"]},
];

export function selectTemplate(facts: string[], occasion: string): string {
  const text = facts.join(" ").toLowerCase();
  if (occasion === "christmas") {
    if (/agi|ai|replace|automation/.test(text)) return "xmas_ai_card";
    return "xmas_santa_automated";
  }
  if (occasion === "birthday" && /\d+/.test(text)) return "incident_report";
  if (/agi|replace|worry|stress/.test(text)) return "thought_bubble";
  if (/work|job|office|manager/.test(text)) return "performance_review";
  return "pet_standup";
}
