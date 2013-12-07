# revision 29901
# category Package
# catalog-ctan /macros/latex/contrib/breakurl
# catalog-date 2013-04-12 10:31:24 +0200
# catalog-license lppl
# catalog-version 1.40
Name:		texlive-breakurl
Version:	1.40
Release:	3
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

%description
This package provides a command much like hyperref's \url that
typesets a URL using a typewriter-like font. However, if the
dvips driver is being used, the original \url doesn't allow
line breaks in the middle of the created link: the link comes
in one atomic piece. This package allows such line breaks in
the generated links.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/breakurl/breakurl.sty
%doc %{_texmfdistdir}/doc/latex/breakurl/README
%doc %{_texmfdistdir}/doc/latex/breakurl/breakurl.pdf
#- source
%doc %{_texmfdistdir}/source/latex/breakurl/breakurl.dtx
%doc %{_texmfdistdir}/source/latex/breakurl/breakurl.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
