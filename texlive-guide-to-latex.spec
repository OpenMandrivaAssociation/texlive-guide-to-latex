# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-guide-to-latex
Version:	20180303
Release:	1
Summary:	TeXLive guide-to-latex package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/guide-to-latex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/guide-to-latex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive guide-to-latex package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/README.txt
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/demo.eps
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/demo.pdf
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/demodoc.pdf
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/demodoc.ps
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/demodoc.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-1.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-10.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-2.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-3.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-4.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-5.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-6.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-7.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-8.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-9.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap11/exer1.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap11/exer11-1.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap11/exer11-2.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap11/exer11-3.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap11/exer11-4.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap11/exer11-5.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap11/exer2.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap11/exer3.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap15/exer15-1.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap15/exer15-2.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap15/exer15-3.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap15/exer15-4.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap15/exer15-5.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap15/exer15-6.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap15/exer15-7.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap2/exer2-1.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap2/exer2-2.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap2/exer2-3a.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap2/exer2-3b.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap2/exer2-3c.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-10.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-11.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-12.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-12.toc
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-1a.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-1b.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-2.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-3.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-4a.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-4b.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-5a.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-5b.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-6.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-7a.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-7b.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-8a.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-8b.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-9.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-1.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-10.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-2.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-3.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-4.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-5.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-6.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-7.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-8.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-9.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap5/exer5-1.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap5/exer5-2.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap5/exer5-3.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap5/exer5-4.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap6/exer6-1.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap6/exer6-2.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap6/exer6-3.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap6/exer6-4.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap6/exer6-5.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-1.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-10.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-11.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-12.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-13.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-14.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-15.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-16.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-17.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-18.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-19.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-2.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-20.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-21a.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-21b.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-3.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-4.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-5.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-6.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-7.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-8.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-9.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap8/exer8-1.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap8/exer8-2.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap8/exer8-3.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/mpletter.cls
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/palette.pdf
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/palette.ps
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/palette.tex
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/seminar.con
%doc %{_texmfdistdir}/doc/latex/guide-to-latex/sempdftx.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 752453
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718591
- texlive-guide-to-latex
- texlive-guide-to-latex
- texlive-guide-to-latex
- texlive-guide-to-latex

