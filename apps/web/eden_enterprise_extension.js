// Add these applications after the APPS and A definitions in the browser prototype.
// All panels are demonstrations, not live OS security controls.
A('identity','Identity Guardian','🔑','Offboarding · Credentials · Access verification',[
 ['l','Offboarding checklist',[['Sessions','Revoke at departure'],['Shared passwords','Rotate with approval'],['Cloud roles','Review and revoke'],['Banking access','Verify at provider'],['Service accounts','Audit delegation'],['Evidence','Preserve logs']]],
 ['t','Policy preview',['Require two-person approval','Review dormant accounts','Alert on failed revocation']],
 ['b','Review workflow',['Start offboarding review','Verify access inventory','Export review summary']]]);
A('finance','Financial Integrity','💳','Reconcile · Investigate · Preserve evidence',[
 ['l','Financial controls',[['Payments','Separate initiation and approval'],['Bank reconciliation','Independent verification'],['Beneficiaries','Secondary approval'],['Audit records','Tamper-evident storage'],['Anomalies','Human review required']]],
 ['t','Policy preview',['Dual payment approval','Independent reconciliation','Protect audit logs']],
 ['b','Review workflow',['Open sample case','Review discrepancies','Export audit checklist']]]);
A('devstudio','EDEN Developer Studio','🧩','Design · Code · Test · Package .obs',[
 ['x','manifest.json','{\\n  "id": "org.cyberpulse.example",\\n  "name": "Example OBS App",\\n  "version": "0.1.0",\\n  "entry": "main.py",\\n  "permissions": []\\n}'],
 ['l','Toolchain',[['Python','App templates'],['Images','Visual specifications'],['.obs','Prototype package format'],['Tests','Isolated build target'],['Signing','Planned']]],
 ['b','Project workflow',['New app project','Review manifest','Validate package']]]);
A('package','OBS Package Manager','📦','Install · Verify · Isolate',[
 ['l','Trust controls',[['Publisher','Verify signature'],['Permissions','Review before installation'],['Dependencies','Check runtime'],['Sandbox','Least privilege'],['Rollback','Known-good version']]],
 ['t','Policy preview',['Require signatures','Review privileged apps','Enable rollback']],
 ['b','Package workflow',['Inspect manifest','Validate sample package','Review policy']]]);
