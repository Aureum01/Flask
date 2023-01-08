#include <iostream>
#include <fstream>
#include <curl/curl.h>

int main() {
  CURL *curl;
  CURLcode res;
  FILE *fp;
  char *url = "https://www.youtube.com/watch?v=<video_id>";
  char outfilename[FILENAME_MAX] = "video.mp4";
  curl = curl_easy_init();
  if (curl) {
    fp = fopen(outfilename,"wb");
    curl_easy_setopt(curl, CURLOPT_URL, url);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, NULL);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, fp);
    curl_easy_setopt(curl, CURLOPT_NOPROGRESS, 0L);
    curl_easy_setopt(curl, CURLOPT_XFERINFOFUNCTION, progress_func);
    res = curl_easy_perform(curl);
    if (res != CURLE_OK) {
      fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
    }
    /* always cleanup */
    curl_easy_cleanup(curl);
    fclose(fp);
  }
  return 0;
}

static int progress_func(void *p, double dltotal, double dlnow, double ultotal, double ulnow)
{
  CURL *curl = (CURL *)p;
  double curtime = 0;

  curl_easy_getinfo(curl, CURLINFO_TOTAL_TIME, &curtime);

  std::cout << "Total time: " << curtime << std::endl;
  std::cout << "Percentage: " << dlnow/dltotal*100 << std::endl;

  return 0;
}
