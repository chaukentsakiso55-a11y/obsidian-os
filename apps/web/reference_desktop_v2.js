/* OBSIDIAN reference-driven desktop enhancement v2.
 * Include after the original browser prototype's app registry and before desktop build().
 * Reference images live in assets/reference_00.png ... reference_16.png.
 * Browser prototype only; no host OS access.
 */
const REFERENCE_LABELS=[
'Desktop and launcher','Boot screen','Boot loading','Desktop applications',
'EDEN AI','Cybersecurity Center','Privacy Center','System Monitor',
'File Manager','Terminal and Developer Studio','Network Control','Settings',
'Security and media screens','Store and virtual machines',
'Storage and power screens','EDEN and developer screens','Hidden settings screens'
];
A('gallery','Visual Reference Gallery','🖼️','17 original design references',null);
A('integrity','Financial Integrity Guardian','💠','Reconciliation · Dual approval · Evidence',[
 ['l','Financial controls',[['Payments','Separate initiation and approval'],['Reconciliation','Independent verification'],['Audit logs','Tamper-evident retention'],['Anomalies','Human review required']]],
 ['t','Demo policy',['Require dual approval','Protect audit records','Flag beneficiary changes']]]);
A('offboard','Identity Guardian','🔐','Offboarding · Credentials · Access',[
 ['l','Departure controls',[['Accounts','Disable and verify'],['Sessions','Revoke tokens'],['Shared secrets','Rotate'],['Service accounts','Review delegation'],['Banking roles','Remove authorizations']]],
 ['t','Demo policy',['Verify departure checklist','Alert on dormant accounts']]]);
A('studio','EDEN Developer Studio','⌘','Code · Design · Package .obs',[
 ['l','SDK roadmap',[['obs init','Create project'],['obs validate','Validate manifest'],['obs build','Assemble package'],['obs verify','Verify publisher']]],
 ['t','Safe build defaults',['Isolate generated code','Review permissions','Require signing']]]);
A('obspkg','OBS Package Manager','📦','Signed apps · Sandbox · Rollback',[
 ['l','Trust controls',[['Manifest','Validate metadata'],['Publisher','Verify signature'],['Permissions','Require approval'],['Sandbox','Least privilege'],['Rollback','Known-good release']]]]);
for(const id of ['gallery','integrity','offboard','studio','obspkg'])APPS[id].nd=0;
const openReferenceGallery=()=>{
 const target=wins.gallery?.el.querySelector('.wb');if(!target)return;
 const render=()=>{target.replaceChildren();
 const title=document.createElement('h3');title.textContent='Original OBSIDIAN screen references';target.append(title);
 const grid=document.createElement('div');grid.className='ob-ref-gallery';target.append(grid);
 REFERENCE_LABELS.forEach((label,i)=>{
 const button=document.createElement('button');button.className='ob-ref-item';
 const img=document.createElement('img');img.loading='lazy';img.src='assets/reference_'+String(i).padStart(2,'0')+'.png';img.alt=label;
 const text=document.createElement('span');text.textContent=label;button.append(img,text);
 button.onclick=()=>{target.replaceChildren();const back=document.createElement('button');back.className='b';back.textContent='← All references';back.onclick=render;const full=document.createElement('img');full.className='ob-ref-large';full.src=img.src;full.alt=label;target.append(back,full)};
 grid.append(button);
 })};render();
};
const obsOriginalOpen=op;
op=function(id){obsOriginalOpen(id);if(id==='gallery')openReferenceGallery()};
