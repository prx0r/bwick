export function generateJokes(templateId: string, recipient: string, facts: string[],
  occasion: string, roast: string, petName?: string, petSpecies?: string, count = 3) {
  const p = petName || "your pet";
  const sp = petSpecies || "pet";
  const r = recipient;
  const edge = roast === "savage" ? 0.9 : roast === "roast" ? 0.6 : 0.3;

  const pools: Record<string, {setup:string;punchline:string;visual:string;tone:string[]}[]> = {
    thought_bubble: [
      {setup:r+"'s biggest worry right now",punchline:p+"'s biggest worry: the treat jar might be at 73% capacity",visual:r+" stressed; "+p+" staring at treat cupboard",tone:["dry","contrast"]},
      {setup:r+': "What if everything falls apart?"',punchline:p+': "What if the squirrel doesn\'t come back tomorrow?"',visual:r+" pacing; "+p+" watching window",tone:["absurdist","contrast"]},
    ],
    pet_standup: [
      {setup:'So '+r+' calls themselves a "pet parent"',punchline:"Ma'am, you forgot to feed me on Tuesday. And Wednesday. I counted.",visual:p+" at stand-up mic, deadpan",tone:["dry","roast"]},
      {setup:"I've been living with "+r+" for a while now",punchline:"The rent is affection and the landlord is deeply unreliable.",visual:p+" on stage with mic",tone:["observational","dry"]},
      {setup:r+' says I\'m their "best friend"',punchline:'Best friend doesn\'t Google "why does my '+sp+' stare at the wall for 40 minutes"',visual:p+" at mic",tone:["roast","specific"]},
    ],
    breaking_news: [
      {setup:"BREAKING: "+r+" spotted doing something competent",punchline:'Witnesses report "mild shock." '+p+" unavailable for comment.",visual:"News broadcast layout",tone:["satirical","dry"]},
      {setup:"ALERT: "+r+" just told a lie",punchline:'"I\'ll be home in 5 minutes," says the person gone 3 hours. '+p+" is not amused.",visual:"Breaking news chyron",tone:["relatable","roast"]},
    ],
    performance_review: [
      {setup:"ANNUAL PERFORMANCE REVIEW \u2014 "+r,punchline:"Food Delivery: Inconsistent. Walks: Cancelled 3x. Belly Rubs: Adequate but not proactive.",visual:p+" with tiny clipboard",tone:["corporate","dry"]},
      {setup:"EMPLOYEE EVALUATION: "+r,punchline:"Strengths: Opens treat bags. Weaknesses: Everything else.",visual:p+" in HR chair",tone:["corporate","roast"]},
    ],
    pet_therapist: [
      {setup:"Dr. "+p+", Licensed Therapist",punchline:'Session notes: Owner exhibits "saying one more episode" syndrome. Prognosis: terminal.',visual:p+" in tiny glasses",tone:["clinical","dry"]},
      {setup:p+"'s assessment of "+r,punchline:`"Your phone distresses your ${sp}. I recommend chin scratches."`,visual:p+" IS the therapist",tone:["warm","dry"]},
    ],
    search_history: [
      {setup:p+"'s recent searches:",punchline:`"how to report owner for late dinner"\n"can ${sp}s legally change families"\n"why human say one more minute for 40 minutes"`,visual:"Browser search bar",tone:["absurdist","relatable"]},
    ],
    complaint_dept: [
      {setup:"FORMAL COMPLAINT \u2014 FILED BY "+p.toUpperCase(),punchline:"Subject: "+r+". Charges: Chronic late-feeding, excessive phone usage.",visual:p+" filling complaint with paw",tone:["corporate","roast"]},
    ],
    split_panel: [
      {setup:r+`'s priority: "Will AGI take my job?"\n${p}'s priority: "Will the squirrel come back tomorrow?"`,punchline:"",visual:"Split panel",tone:["contrast","topical"]},
    ],
    incident_report: [
      {setup:"INCIDENT REPORT",punchline:"Subject has completed another revolution. Functional decline noted. "+p+" filed a complaint.",visual:"Official report with paw print",tone:["corporate","dry"]},
    ],
    wildcard: [
      {setup:"We saw your "+sp+" and had questions.",punchline:"Here are the answers you didn't know you needed about "+r+".",visual:"Depends on generation",tone:["meta","warm"]},
    ],
    xmas_santa_automated: [
      {setup:"Merry Christmas!",punchline:"Your role has been automated.",visual:"Santa reading notice",tone:["corporate","dry","topical"]},
      {setup:"Merry Christmas, "+r+".",punchline:"Your role has been automated. Please do not reply. Seasonal decisions are final.",visual:"Santa with notice",tone:["corporate","satirical"]},
    ],
    xmas_santa_vs_robots: [{setup:"BREAKING: 10 million robots disabled",punchline:"In unexplained sleigh-based overnight attack.",visual:"Robot wreckage",tone:["satirical","topical"]}],
    xmas_elf_redundancy: [{setup:"MEMO: North Pole Restructuring",punchline:"Following agent deployment, 47 elf positions eliminated.",visual:"Corporate memo",tone:["corporate","topical"]}],
    xmas_pet_security: [{setup:"SECURITY INCIDENT REPORT",punchline:"STRANGER ENTERED HOME VIA CHIMNEY. DOG ACCEPTED BISCUIT. INVESTIGATION CLOSED.",visual:"Security report",tone:["corporate","dry"]}],
    xmas_performance_review: [{setup:"CHRISTMAS REVIEW: "+r,punchline:"Turkey: adequate. Walks: unacceptable. Wrapping: embarrassing.",visual:p+" with clipboard",tone:["corporate","dry"]}],
    xmas_human_vs_pet: [{setup:`Human: "Will Christmas still feel human after AGI?"\n${p}: "Turkey"`,punchline:"",visual:"Split panel",tone:["contrast","topical"]}],
    xmas_cat_vs_tree: [{setup:"INCIDENT REPORT",punchline:"Decorative structure destroyed less than 14 minutes after deployment.",visual:"Broken tree",tone:["documentary","dry"]}],
    xmas_santa_search_history: [{setup:"Santa just read "+r+"'s search history:",punchline:`"is santa edible"\n"reindeer territorial rights"\n"how to remove tinsel from digestive tract"`,visual:"Santa horrified",tone:["absurdist","pet"]}],
    xmas_ai_card: [{setup:`Human: "Will Christmas still feel human after AGI?"\n${p}: "You bought this card from an AI"`,punchline:"",visual:"Meta card",tone:["meta","topical","dry"]}],
    xmas_pet_complaint: [{setup:"FORMAL COMPLAINT TO: Santa Claus",punchline:"Requesting replacement owner. Current unit misses scheduled feeding windows.",visual:p+" writing letter",tone:["corporate","dry"]}],
  };

  const pool = pools[templateId] || pools.wildcard;
  return pool.slice(0, count).map((j, i) => ({
    id: templateId+"_c"+(i+1), template_id: templateId,
    setup: j.setup, punchline: j.punchline, visual: j.visual,
    tone: j.tone, edge,
  }));
}
