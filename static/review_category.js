 function categoryChange(e) {
                        var area_a = ["선유도공원","하늘공원","아차산정상"];
                        var area_b = ["탄도항","궁평리마을"];
                        var area_c = ["민머루해수욕장","동막해수욕장","을왕리해수욕장","영종도","마시안해변"];
                        var area_d = ["하조대","남애항","정동진해변","태백산","추암해수욕장"];
                        var area_e = ["도담상봉"];
                        var area_f = ["왜목마을","간월암","꽃지해안공원","마량포해돋이마을"];
                        var area_g = ["변산반도","채석강","곰소항"];
                        var area_h = ["도리포","순천만","향일암","세방낙조전망대","남열해수욕장","땅끝마을","완도타워"];
                        var area_i = ["부석사","망양정","호미곶","읍천항","삼사해상공원","혼신지"];
                        var area_j = ["우포늪","지리산 천왕봉","보리암"];
                        var area_k = ["강양항","간절곶"];
                        var area_l = ["죽성성당","다대포"];
                        var area_m = ["울릉도","독도"];



                        var target = document.getElementById("where");

                        if (e.value == "서울") var d = area_a;
                        else if (e.value == "경기") var d = area_b;
                        else if (e.value == "인천") var d = area_c;
                        else if (e.value == "강원") var d = area_d;
                        else if (e.value == "충북") var d = area_e;
                        else if (e.value == "충남") var d = area_f;
                        else if (e.value == "전북") var d = area_g;
                        else if (e.value == "전남") var d = area_h;
                        else if (e.value == "경북") var d = area_i;
                        else if (e.value == "경남") var d = area_j;
                        else if (e.value == "울산") var d = area_k;
                        else if (e.value == "부산") var d = area_l;
                        else if (e.value == "울릉군") var d = area_m;

                        target.options.length = 0;

                        for (x in d) {
                            var opt = document.createElement("option");
                            opt.value = d[x];
                            opt.innerHTML = d[x];
                            target.appendChild(opt);
                        }
                    }