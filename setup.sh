

mkdir assignment$1
sed -r "s/title\{\}/title\{Assignment $1\}/" template.tex > assignment${1}/a${1}.tex
git add assignment$1/a$1.tex
sed -r -i "s/A_NUM: [[:digit:]]+$/A_NUM: $1/" .travis.yml