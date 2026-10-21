<?php
// Stubbed-WordPress test harness for instatech-seo-fixes.php.
// Run: php instatech/wp/tests/harness.php instatech/wp/mu-plugins/instatech-seo-fixes.php
define('ABSPATH','/x/');
$F=[]; function add_filter($h,$cb,$p=10,$n=1){global $F;$F[$h][]=[$cb,$n];}
function add_action($h,$cb,$p=10,$n=1){} function untrailingslashit($s){return rtrim($s,'/');} function is_front_page(){return false;} function is_page(){return false;}
function apply($h,...$a){global $F;foreach($F[$h] as [$cb,$n]){$a[0]=$cb(...array_slice($a,0,$n));}return $a[0];}
$CTX=['admin'=>false,'post'=>(object)['post_name'=>'desktop-computer-repair-near-me'],'tax'=>null,'cat'=>false,'prod'=>false,'title'=>'EnergyBar T20 20,000mAh'];
function is_admin(){global $CTX;return $CTX['admin'];} function get_post(){global $CTX;return $CTX['post'];}
function home_url(){return 'https://instatech.uk';} function trailingslashit($s){return rtrim($s,'/').'/';}
function esc_url($u){return $u;} function wp_unslash($s){return $s;} function wp_strip_all_tags($s){return strip_tags($s);}
function is_category($s=null){global $CTX;return $s? $CTX['cat']===$s : (bool)$CTX['cat'];}
function is_tax($t){global $CTX;return $CTX['tax']===$t;} function is_singular($t){global $CTX;return $CTX['prod'];}
function get_queried_object(){return (object)['name'=>'Power Bank'];} function get_the_title($id=0){global $CTX;return $id===5?'Quad USB-C Hub':$CTX['title'];}
function in_the_loop(){return false;}
require $argv[1];
$html='<a href="https://instatech.uk/electronics-repair-2/">x</a> <a href="/request-quote">y</a> <a href=\'https://instatech.uk/testimonials/#a\'>z</a> <a href="https://instatech.uk/mobile-repair-services/">ok</a> <a href="https://other.com/electronics-store-1/">ext</a>';
echo apply('the_content',$html),"\n";
$CTX['post']=(object)['post_name'=>'why-is-my-phone-battery-draining']; echo apply('the_content','<a href="https://instatech.uk/electronics-repair-2/">x</a>'),"\n";
$_SERVER['REQUEST_URI']='/layouts/battery/'; print_r(apply('rank_math/frontend/robots',['index'=>'index','follow'=>'follow']));
$_SERVER['REQUEST_URI']='/'; $CTX['cat']='uncategorized'; print_r(apply('rank_math/frontend/robots',['index'=>'index']));
$CTX['cat']=false;$CTX['tax']='product_cat'; echo apply('rank_math/frontend/description',''),"\n";
$CTX['tax']=null;$CTX['prod']=true; echo apply('rank_math/frontend/description',''),"\n"; echo apply('rank_math/frontend/description','Existing desc'),"\n";
echo apply('rank_math/frontend/title','Phone Repair Moorgate | instaTech'),"\n";
echo json_encode(apply('rank_math/json_ld',['publisher'=>['@type'=>'Organization','name'=>'InstaTech'],'x'=>['@type'=>['MobilePhoneStore','LocalBusiness'],'sameAs'=>['a']], 'y'=>['@type'=>['Organization','Place'],'sameAs'=>'https://www.tiktok.com/@instatechlondon']])),"\n";
print_r(apply('wp_get_attachment_image_attributes',['alt'=>''],(object)['post_parent'=>5,'post_title'=>'img-01']));
print_r(apply('wp_get_attachment_image_attributes',['alt'=>'kept'],(object)['post_parent'=>5,'post_title'=>'img-01']));
