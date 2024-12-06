from spack.package import *


class PyCmd2(PythonPackage):
    """cmd2 is a tool for building interactive command line applications in Python."""

    homepage = "https://cmd2.readthedocs.io/en/stable/"
    pypi = "cmd2/cmd2-2.5.7.tar.gz"

    maintainers("rtrigg")

    license("MIT", checked_by="rtrigg")

    version("2.5.7", sha256="0219e2bb75075fa16deffb88edf86efdd2a87439d1fa7b94fdea4b929a3dc914")
    version("2.5.6", sha256="ab0ff178784ca087d886081b2ca384724c90b9b25eb982c57c6925ca17479f52")
    version("2.5.5", sha256="adc9a7f1933da9c5b2ae939d54c9d4247be0b46a0e847de02ccf829ce2827cb4")
    version("2.5.0", sha256="36292d144e5fd62549b50e94e5f36514557fb92e615155ac28763ea4bc13b954")
    version("2.4.3", sha256="71873c11f72bd19e2b1db578214716f0d4f7c8fa250093c601265a9a717dee52")
    version("2.3.3", sha256="750d7eb04d55c3bc2a413e191bc177856f388102de47d11f2210a35266543640")

    variant("test", default=False, description="Run package's test suite")

    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm@8:", type="build")

    depends_on("py-pyperclip", type=("build", "run"))
    depends_on("py-wcwidth", type=("build", "run"))
    depends_on("readline", when="platform=darwin", type=("build", "run"))

    depends_on("py-pytest", type=("build", "run"), when="+test")
    depends_on("py-pytest-cov", type=("build","run"), when="+test")
    depends_on("py-pytest-mock", type=("build","run"), when="+test")

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def check_build(self):
        pytest = which("pytest")
        pytest()
