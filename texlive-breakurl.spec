# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/breakurl
# catalog-date 2009-09-27 09:44:19 +0200
# catalog-license lppl
# catalog-version 1.30
Name:		texlive-breakurl
Version:	1.30
Release:	1
Summary:	Line-breakable \url-like links in hyperref when compiling via dvips/ps2pdf
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/breakurl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/breakurl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/breakurl.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/breakurl.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package provides a command much like hyperref's \url that
typesets a URL using a typewriter-like font. However, if the
dvips driver is being used, the original \url doesn't allow
line breaks in the middle of the created link: the link comes
in one atomic piece. This package allows such line breaks in
the generated links.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/breakurl/breakurl.sty
%doc %{_texmfdistdir}/doc/latex/breakurl/README
%doc %{_texmfdistdir}/doc/latex/breakurl/breakurl.pdf
#- source
%doc %{_texmfdistdir}/source/latex/breakurl/breakurl.dtx
%doc %{_texmfdistdir}/source/latex/breakurl/breakurl.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
