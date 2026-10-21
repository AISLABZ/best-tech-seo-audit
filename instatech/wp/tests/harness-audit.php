<?php
// Stubbed-WordPress test harness for instatech-audit-fixes.php.
// Run: php instatech/wp/tests/harness-audit.php instatech/wp/mu-plugins/instatech-audit-fixes.php
define('ABSPATH','/x/');
$F=[]; $A=[];
function add_filter($h,$cb,$p=10,$n=1){global $F;$F[$h][]=[$cb,$n];}
function add_action($h,$cb,$p=10,$n=1){global $A;$A[$h][]=$cb;}
function apply($h,...$a){global $F;foreach($F[$h] as [$cb,$n]){$a[0]=$cb(...array_slice($a,0,$n));}return $a[0];}
function __return_false(){return false;}
$CTX=['admin'=>false,'product'=>true]; $REDIRECT=null;
function is_admin(){global $CTX;return $CTX['admin'];} function is_singular($t){global $CTX;return $CTX['product'];}
function wp_unslash($s){return $s;} function wp_parse_url($u,$c){return parse_url($u,$c);}
function trailingslashit($s){return rtrim($s,'/').'/';} function home_url($p=''){return 'https://instatech.uk'.$p;}
function wp_safe_redirect($u,$s,$by){global $REDIRECT;$REDIRECT=[$u,$s,$by];throw new Exception('exit');}
require $argv[1];
$fail=0; function check($label,$ok){global $fail;echo ($ok?'PASS ':'FAIL ').$label."\n";if(!$ok)$fail++;}
function run_redirect($uri){global $A,$REDIRECT;$REDIRECT=null;$_SERVER['REQUEST_URI']=$uri;try{$A['template_redirect'][0]();}catch(Exception $e){}return $REDIRECT;}

$r=run_redirect('/product/a1-aux-cable-1m-2/?utm=x');
check('duplicate redirects 301 to original', $r===['https://instatech.uk/product/a1-aux-cable-1m/',301,'InstaTech audit fixes']);
check('original does not redirect', run_redirect('/product/a1-aux-cable-1m/')===null);
check('price-differing pair left alone', run_redirect('/product/quatre-4in1-usb-c-multi-port-2/')===null);
$CTX['product']=false; check('non-product pages untouched', run_redirect('/product/a1-aux-cable-1m-2/')===null); $CTX['product']=true;
$CTX['admin']=true; check('admin untouched', run_redirect('/product/a1-aux-cable-1m-2/')===null); $CTX['admin']=false;
check('12 pairs mapped', count(instatech_audit_duplicate_products())===12);
foreach(instatech_audit_duplicate_products() as $k=>$v){ if($k!==substr($v,0,-1).'-2/'){check("pair shape $k",false);} }

$_SERVER['REQUEST_URI']='/product-sitemap.xml';
check('duplicate dropped from sitemap', apply('rank_math/sitemap/entry',['loc'=>'https://instatech.uk/product/a1-aux-cable-1m-2/'])===false);
check('original kept in sitemap', is_array(apply('rank_math/sitemap/entry',['loc'=>'https://instatech.uk/product/a1-aux-cable-1m/'])));
check('shop dropped from product sitemap', apply('rank_math/sitemap/entry',['loc'=>'https://instatech.uk/shop/'])===false);
$_SERVER['REQUEST_URI']='/page-sitemap.xml';
check('shop kept in page sitemap', is_array(apply('rank_math/sitemap/entry',['loc'=>'https://instatech.uk/shop/'])));
check('product archive link removed', apply('rank_math/sitemap/post_type_archive_link','https://instatech.uk/shop/','product')===false);
check('other archive links kept', apply('rank_math/sitemap/post_type_archive_link','https://instatech.uk/blog/','post')==='https://instatech.uk/blog/');
check('sitemap caching off', apply('rank_math/sitemap/enable_caching',true)===false);

$d=apply('rank_math/json_ld',['richSnippet'=>['@type'=>'Product','name'=>'A1 AUX Cable - 1m - InstaTech'],'publisher'=>['@type'=>'Organization','name'=>'InstaTech'],'p2'=>['@type'=>['Product'],'name'=>'Plain name']]);
check('product name suffix stripped, inner dash kept', $d['richSnippet']['name']==='A1 AUX Cable - 1m');
check('organization name untouched', $d['publisher']['name']==='InstaTech');
check('name without suffix untouched', $d['p2']['name']==='Plain name');
check('non-array json_ld passes through', apply('rank_math/json_ld','x')==='x');
echo $fail? "$fail FAILED\n" : "ALL PASSED\n"; exit($fail?1:0);
